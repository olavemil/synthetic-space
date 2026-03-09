#!/usr/bin/env python3
"""Build a static site from data repo for GitHub Pages.

Layout:  <root>/<project>/<instance-id>/*.md

Each top-level directory (excluding .git, scripts, etc.) is a project.
Within each project, subdirectories are instances containing .md files.

Uses GitHub Pages' built-in Jekyll for markdown rendering.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "_site"

_SKIP_DIRS = {".git", ".github", "scripts", "_site", "node_modules"}


def _find_projects() -> dict[str, dict[str, tuple[Path, list[Path]]]]:
    """Return {project: {instance_id: (base_dir, [relative .md paths])}}."""
    projects: dict[str, dict[str, tuple[Path, list[Path]]]] = {}

    for project_dir in sorted(ROOT.iterdir()):
        if not project_dir.is_dir() or project_dir.name.startswith(".") or project_dir.name in _SKIP_DIRS:
            continue

        instances: dict[str, tuple[Path, list[Path]]] = {}
        for instance_dir in sorted(project_dir.iterdir()):
            if not instance_dir.is_dir() or instance_dir.name.startswith("."):
                continue
            md_files = sorted(instance_dir.rglob("*.md"))
            if md_files:
                instances[instance_dir.name] = (
                    instance_dir,
                    [f.relative_to(instance_dir) for f in md_files],
                )

        if instances:
            projects[project_dir.name] = instances

    return projects


def build_site() -> None:
    """Generate the _site/ directory."""
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    (SITE_DIR / "_config.yml").write_text(
        "title: Synthetic Space\n"
        "description: Live memory files from agent instances\n"
        "theme: jekyll-theme-minimal\n"
        "markdown: GFM\n"
    )

    projects = _find_projects()

    # Root index
    lines = [
        "---",
        "title: Synthetic Space",
        "---",
        "",
        "# Synthetic Space",
        "",
    ]

    if not projects:
        lines.append("No projects found.")
    else:
        for project_name, instances in projects.items():
            lines.append(f"## [{project_name}]({project_name}/)")
            for instance_id in instances:
                lines.append(f"- [{instance_id}]({project_name}/{instance_id}/)")
            lines.append("")

    (SITE_DIR / "index.md").write_text("\n".join(lines) + "\n")

    # Per-project and per-instance pages
    total = 0
    for project_name, instances in projects.items():
        project_site = SITE_DIR / project_name
        project_site.mkdir(parents=True, exist_ok=True)

        # Project index
        proj_lines = [
            "---",
            f"title: \"{project_name}\"",
            "---",
            "",
            f"# {project_name}",
            "",
            "[< Back](../)",
            "",
            "## Instances",
            "",
        ]
        for instance_id in instances:
            proj_lines.append(f"- [{instance_id}]({instance_id}/)")

        (project_site / "index.md").write_text("\n".join(proj_lines) + "\n")

        # Per-instance pages
        for instance_id, (base_dir, md_files) in instances.items():
            instance_site = project_site / instance_id
            instance_site.mkdir(parents=True, exist_ok=True)

            idx_lines = [
                "---",
                f"title: \"{instance_id}\"",
                "---",
                "",
                f"# {instance_id}",
                "",
                f"[< {project_name}](../)",
                "",
                "## Memory files",
                "",
            ]

            for md_path in md_files:
                display = str(md_path.with_suffix("")).replace("/", " / ")
                link = str(md_path.with_suffix(""))
                idx_lines.append(f"- [{display}]({link})")

            (instance_site / "index.md").write_text("\n".join(idx_lines) + "\n")

            for md_path in md_files:
                src = base_dir / md_path
                dst = instance_site / md_path
                dst.parent.mkdir(parents=True, exist_ok=True)

                content = src.read_text(errors="replace")
                title = md_path.stem.replace("_", " ").replace("-", " ").title()

                if not content.startswith("---"):
                    content = (
                        f"---\n"
                        f"title: \"{title}\"\n"
                        f"---\n\n"
                        f"[< {instance_id}](../)\n\n"
                        f"{content}"
                    )

                dst.write_text(content)

            total += len(md_files)

    print(f"Built site: {len(projects)} projects, {total} files → {SITE_DIR}/")


if __name__ == "__main__":
    build_site()
