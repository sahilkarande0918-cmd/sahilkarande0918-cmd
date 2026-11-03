# Profile setup
The profile at https://github.com/sahilkarande0918-cmd uses a self-hosted SVG banner and clickable custom project cards. GitHub Actions refresh analytics and the snake animation daily. No personal access token is required for the installed workflows. If generated assets are not appearing, check the Actions tab, repository Actions permissions, and workflow logs. The dashboard workflow creates assets/overview.dark.svg, languages.dark.svg, contributions.dark.svg, momentum.dark.svg, cadence.dark.svg. The snake workflow publishes an output branch. Avoid hard-coded or invented statistics.

## Updated contribution visuals
- The charts are full width and render as SVGs from repository files.
- The animated heatmap action generates `activity-graph.svg` and `activity-graph-mobile.svg` daily, with a green animated theme, so the README has no dependency on a hosted activity-graph image service.
- The profile-cards action now also generates `assets/lifetime.dark.svg` automatically.
- `Contributions (all time)` reflects contributions the GitHub GraphQL API exposes to the workflow. Private contributions may not be included; do not hardcode an unverified figure. To reveal anonymized private contribution counts, use GitHub profile > Contribution settings > Private contributions. The GitHub stats continue to update from the source daily.
