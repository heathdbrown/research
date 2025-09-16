import os
from pathlib import Path

REPO_ROOT = Path("./")
README_PATH = REPO_ROOT / "README.md"


def get_md_files(root: Path) -> list[Path]:
    md_files = list(root.glob("**/*.md"))
    return sorted(md_files)


def make_toc(md_files: list[Path]) -> dict:
    toc_tree = {}
    for path in md_files:
        parts = path.parts
        if "README.md" in parts:
            continue
        current_level = toc_tree
        for part in parts[:-1]:
            current_level = current_level.setdefault(part, {})
        current_level[parts[-1]] = str(path).replace(os.sep, "/")
    return toc_tree


def render_toc(tree, indent=0):
    lines = []
    for key, value in tree.items():
        if isinstance(value, dict):
            # Render category header (as bold or just indented)
            lines.append(f"# {key.title()}")
            lines.extend(render_toc(value))
        else:
            # Render link
            name = key.replace("_", " ").replace("-", " ").strip(".md").title()
            lines.append("  " * indent + f"- [{name}]({value})")
    return lines


def main():
    print("Building table of contents...")
    print(REPO_ROOT)
    md_files = get_md_files(REPO_ROOT)
    toc_lines = ["# Table of contents\n"] + render_toc(make_toc(md_files))
    toc = "\n".join(toc_lines)
    print(f"Generated TOC with {len(md_files)} files.")
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(toc)
    print(f"Table of contents written to {README_PATH}")


if __name__ == "__main__":
    main()
