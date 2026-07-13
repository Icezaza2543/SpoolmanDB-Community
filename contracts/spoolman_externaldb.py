"""Reviewed AST-only snapshot of Spoolman's external filament data contract.

Source: https://github.com/Donkie/Spoolman/blob/470d8f3bcc0c910ec4e994d526de841098883b11/spoolman/externaldb.py
This file is parsed but never imported or executed by the compatibility checker.
"""

from collections.abc import Iterator
from enum import Enum

from pydantic import BaseModel, Field, RootModel


class SpoolType(Enum):
    PLASTIC = "plastic"
    CARDBOARD = "cardboard"
    METAL = "metal"


class Finish(Enum):
    MATTE = "matte"
    GLOSSY = "glossy"


class MultiColorDirection(Enum):
    COAXIAL = "coaxial"
    LONGITUDINAL = "longitudinal"


class Pattern(Enum):
    MARBLE = "marble"
    SPARKLE = "sparkle"


class ExternalFilament(BaseModel):
    id: str = Field(description="A unique ID for this filament.")
    manufacturer: str = Field(description="Filament manufacturer.")
    name: str = Field(description="Filament name.")
    material: str = Field(description="Filament material.")
    density: float = Field(description="Density in g/cm3.")
    weight: float = Field(description="Net weight of a single spool.")
    spool_weight: float | None = Field(
        default=None,
        description="Weight of an empty spool.",
    )
    spool_type: SpoolType | None = Field(
        None,
        description="Type of spool.",
    )
    diameter: float = Field(description="Filament in mm.")
    color_hex: str | None = Field(
        default=None,
        description="Filament color code for single-color filaments.",
    )
    color_hexes: list[str] | None = Field(
        default=None,
        description="Color codes for multi-color filaments.",
    )
    extruder_temp: int | None = Field(
        default=None,
        description="Extruder/nozzle temperature in °C.",
    )
    bed_temp: int | None = Field(
        default=None,
        description="Bed temperature in °C.",
    )
    finish: Finish | None = Field(
        default=None,
        description="Finish of the filament.",
    )
    multi_color_direction: MultiColorDirection | None = Field(
        default=None,
        description="Direction of multi-color filaments.",
    )
    pattern: Pattern | None = Field(
        default=None,
        description="Pattern of the filament.",
    )
    translucent: bool = Field(
        default=False,
        description="Whether the filament is translucent.",
    )
    glow: bool = Field(
        default=False,
        description="Whether the filament is glow-in-the-dark.",
    )


class ExternalFilamentsFile(RootModel):
    root: list[ExternalFilament]

    def __iter__(self) -> Iterator[ExternalFilament]:
        """Iterate over the filaments."""
        return iter(self.root)

    def __getitem__(self, index: int) -> ExternalFilament:
        """Get a specific filament by index."""
        return self.root[index]
