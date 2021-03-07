#Development pipeline v1.0.0
<br><br>
##Branch: develop
Base branch: Master
Description: Latest state of Development. Post BugFix. (unstable)
<br>
##Branch: feature
Base branch: Develop
Description: Cutting-edge features. Used for any maintenance features / active development(container/web), Docker updates. (unstable)
<br>
##Branch: release-vX.Y.Z
Base branch: Develop
Description: A temporary release branch that follows the <a href="http://semver.org/" rel="nofollow">semver</a> versioning. <br>
A pull request is required to merge code into any release-vX.Y.Z branch.
<br>
##Branch: bug-fix
Base branch: release-vX.Y.Z
Description: Fixes against a release branch. The bug-fix branch should be merged into the release branch and into develop. 
<br>
##Branch: hotfix-*
Base branch: master
Description: [Restricted access] Production bug fixes. * -> Descriptor
