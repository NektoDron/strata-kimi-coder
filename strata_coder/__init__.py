"""Root-level package bridge so `python -m strata_coder.serve` works directly from the strata repo root."""
from pathlib import Path

_pkg_dir = str(Path(__file__).resolve().parent.parent / "python" / "strata_coder")
if _pkg_dir not in __path__:
    __path__.insert(0, _pkg_dir)

from .decoder import (  # noqa: E402,F401
    unpack_sc_lut_indices,
    decode_sc_lut_matrix,
    resolve_optimal_dtype,
)
from .tiered_moe_loader import (  # noqa: E402,F401
    TieredMoECacheManager,
    detect_system_memory_gb,
    load_strata_coder_layer,
    load_strata_coder_multi_gpu,
)
from .engine import KimiCoderEngine  # noqa: E402,F401
