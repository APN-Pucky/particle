# Copyright (c) 2018-2025, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/particle for details.


from __future__ import annotations

import sys

from .corsika import Corsika7ID
from .geant import Geant3ID

# Direct access to Particle literals
# Direct access to Particle (the CSV file is not read until a particle is accessed)
# Direct access to handy LaTeX to HTML particle name conversions
# Direct access to kinematics functions
from .particle import (
    InvalidParticle,
    Particle,
    ParticleNotFound,
    latex_to_html_name,
    lifetime_to_width,
    literals,
    width_to_lifetime,
)
from .particle.enums import Charge, Inv, Parity, SpinType, Status

# Direct access to PDGID and other ID classes
from .pdgid import PDGID
from .pythia import PythiaID

# Convenient access to the version number
from .version import version as __version__

# Literals direct access
sys.modules["particle.literals"] = literals

__all__ = (
    "PDGID",
    "Charge",
    "Corsika7ID",
    "Geant3ID",
    "Inv",
    "InvalidParticle",
    "Parity",
    "Particle",
    "ParticleNotFound",
    "PythiaID",
    "SpinType",
    "Status",
    "__version__",
    "latex_to_html_name",
    "lifetime_to_width",
    "width_to_lifetime",
)


def __dir__() -> tuple[str, ...]:
    return __all__
