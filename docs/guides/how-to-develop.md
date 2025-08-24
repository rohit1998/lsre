# Development

## For quick changes

1. make your changes
1. check and put them in staging area
1. `j pr branch-name commit-message=branch-name` to create branch and pull request run
1. Wait for github actions to pass.
1. Optional, `j pu commit-message` on issue, make changes
1. `j mpr`, finally merge on actions and features success, and cleanup branches.

## For proper features

1. `j b branch-name`, make a branch off main
1. Do changes
1. check and put them in staging area
1. `j pu commit-message`
1. Keep doing until feature is developed.
1. `j cpr` to create pr.
1. Wait for github actions to pass.
1. Optional, `j pu commit-message` on issue, make changes
1. `j mpr`, finally merge on actions and features success, and cleanup branches.
