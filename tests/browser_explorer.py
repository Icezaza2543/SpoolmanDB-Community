"""Optional real-browser QA: python tests/browser_explorer.py --url http://localhost:8000/public/"""

import argparse
from pathlib import Path
import time

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default='http://localhost:8000/public/')
    parser.add_argument('--screenshots', type=Path, default=Path('.git/explorer-qa'))
    parser.add_argument('--browser', choices=['chromium', 'firefox', 'webkit'], default='chromium')
    args = parser.parse_args()
    args.screenshots.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = getattr(playwright, args.browser).launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 1000})
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(args.url + '#explorer')
        page.wait_for_function("document.querySelector('#load-status').textContent.startsWith('Loaded')")
        assert page.locator('.filament-card').count() == 24
        page.select_option('#manufacturer-filter', 'Sunlu')
        page.select_option('#material-filter', 'PETG')
        started = time.perf_counter()
        page.fill('#search', '2.0')
        page.wait_for_function("document.querySelector('#results-summary').textContent.includes('20 matches')")
        print(f'Search/filter response including debounce: {time.perf_counter() - started:.3f}s')
        assert page.locator('.filament-card').count() == 20
        shared = page.url
        page.reload()
        page.wait_for_function("document.querySelector('#load-status').textContent.startsWith('Loaded')")
        assert page.locator('#search').input_value() == '2.0'
        assert page.locator('.filament-card').count() == 20
        page.fill('#search', 'no-such-filament-xyz')
        page.wait_for_function("document.querySelector('#results-summary').textContent.includes('0 matches')")
        assert page.locator('#manufacturer-filter').input_value() == 'Sunlu'
        assert page.locator('#material-filter').input_value() == 'PETG'
        page.get_by_role('button', name='Reset filters', exact=True).click()
        page.wait_for_function("document.querySelector('#search').value === ''")
        page.get_by_role('button', name='Next page', exact=True).click()
        assert '25–48' in page.locator('#results-summary').inner_text()
        page.get_by_role('button', name='Table', exact=True).click()
        assert page.locator('#results-body tr').count() == 24
        page.get_by_role('button', name='Cards', exact=True).click()
        for width, height, label in [(1440, 1000, 'desktop'), (768, 1024, 'tablet'), (390, 844, 'mobile')]:
            page.set_viewport_size({'width': width, 'height': height})
            page.goto(shared)
            page.wait_for_function("document.querySelector('#load-status').textContent.startsWith('Loaded')")
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            page.screenshot(path=str(args.screenshots / f'explorer-{label}.png'), full_page=False)
            page.locator('.filament-card summary').first.focus()
            page.keyboard.press('Enter')
            assert page.locator('.filament-card details').first.get_attribute('open') is not None
            for route in ['home', 'analytics', 'schema', 'contribute']:
                page.locator(f'.nav-link[href="#{route}"]').click()
                page.locator('#' + route).wait_for(state='visible')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        assert not errors, errors
        page.set_viewport_size({'width': 1440, 'height': 1000})
        page.locator('.header-copy').click()
        page.wait_for_timeout(1400)
        assert page.locator('.header-copy .material-symbols-outlined').count() == 1
        # Exercise fetched, untrusted catalog values through the actual DOM.
        hostile = browser.new_page()
        hostile.route('**/filaments.json', lambda route: route.fulfill(json=[{
            'id': 'hostile', 'manufacturer': '<img src=x onerror=alert(1)>',
            'name': '<script>alert(1)</script>', 'material': 'PLA', 'density': 1.24,
            'weight': 1000, 'diameter': 1.75, 'color_hex': 'FFFFFF',
            'tds_url': 'javascript:alert(1)',
        }]))
        hostile.goto(args.url + '#explorer')
        hostile.wait_for_function("document.querySelector('#load-status').textContent.startsWith('Loaded')")
        assert hostile.locator('.filament-card script, .filament-card img, a[href^="javascript:"]').count() == 0
        assert '<script>' in hostile.locator('.filament-card h2').inner_text()
        failed = browser.new_page()
        failed.route('**/filaments.json', lambda route: route.fulfill(status=503, body='Unavailable'))
        failed.goto(args.url + '#explorer')
        failed.wait_for_function("document.querySelector('#results-summary').textContent === 'Catalog unavailable'")
        assert 'reload' in failed.locator('#catalog-cards').inner_text()
        print('PASS: cards, filters, empty state, pagination, deep links, keyboard details, all routes and responsive widths')
        browser.close()


if __name__ == '__main__':
    main()
