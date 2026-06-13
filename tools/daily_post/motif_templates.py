"""Generic motif templates for auto-generated thumbnails.

Each motif is a string containing an SVG <g> element, sized ~300x290 and
positioned around (820, 165). They share the same purple background palette
defined in tools/thumbnails/gen_thumbnails.py.
"""

# Motifs are loaded lazily from .svg files in this same directory so the
# Python module stays small and motifs can be edited as plain SVG.
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_TEMPLATE_DIR = os.path.join(_HERE, "motif_templates")


def _load(name: str) -> str:
    p = os.path.join(_TEMPLATE_DIR, name + ".svg")
    return open(p).read()


def __getattr__(name):
    if name == "GENERIC_MOTIFS":
        return {
            "circuit": _load("circuit"),
            "bubbles": _load("bubbles"),
            "rings": _load("rings"),
            "openbook": _load("openbook"),
            "lock": _load("lock"),
            "dots": _load("dots"),
        }
    raise AttributeError(name)


def pick_motif_key(tags):
    s = " ".join(tags).lower()
    if any(k in s for k in ["工作流", "openclaw", "技术", "runtime", "工作"]):
        return "circuit"
    if any(k in s for k in ["沟通", "对话", "语言", "人际", "群聊"]):
        return "bubbles"
    if any(k in s for k in ["记忆", "记录", "连接", "关系"]):
        return "rings"
    if any(k in s for k in ["写作", "阅读", "创作", "文化"]):
        return "openbook"
    if any(k in s for k in ["隐私", "伦理", "安全", "边界", "著作"]):
        return "lock"
    return "dots"
