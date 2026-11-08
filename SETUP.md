# GitHub profile setup

This repository is the special profile README for [@sahilkarande0918-cmd](https://github.com/sahilkarande0918-cmd).

## Live statistics
The workflow `.github/workflows/profile-cards.yml` runs daily and on appropriate repository changes. It generates only:
- `assets/overview.dark.svg` — live contribution totals, repositories, stars, and followers.
- `assets/contributions.dark.svg` — full-width 3D contribution landscape and streaks.

`scripts/curate_overview.py` removes the Pull requests merged and Issues opened cards after generation, leaving the six desired statistics without hardcoding their numbers.

The contributions shown are those available to the GitHub API for the workflow token and may omit private activity. The rest of the profile uses static assets under `assets/`.

The older expandable "More GitHub history and coding rhythm" section, lifetime/cadence graphics and snake animation were intentionally removed from the public profile. Their scheduled generators are no longer installed.
