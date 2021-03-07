#Development pipeline v1.0.0
<br><br>
##Branch: develop<br>
Base branch: Master<br>
Description: Latest state of Development. Post BugFix. (unstable)
<br>
##Branch: feature<br>
Base branch: Develop<br>
Description: Cutting-edge features. Used for any maintenance features / active development(container/web), Docker updates. (unstable)
<br>
##Branch: release-vX.Y.Z<br>
Base branch: Develop<br>
Description: A temporary release branch that follows the <a href="http://semver.org/" rel="nofollow">semver</a> versioning. <br>
A pull request is required to merge code into any release-vX.Y.Z branch.<br>
<br>
##Branch: bug-fix<br>
Base branch: release-vX.Y.Z<br>
Description: Fixes against a release branch. The bug-fix branch should be merged into the release branch and into develop. <br>
<br>
##Branch: hotfix-*<br>
Base branch: master<br>
Description: [Restricted access] Production bug fixes. * -> Descriptor<br>
