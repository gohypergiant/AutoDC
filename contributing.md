## Contribution guidelines

This guide documents the best way to make contributions to the AutoDC projects, including 
how to create a pull request and code review process. Contributors are also encouraged to 
review [code of conduct](https://github.com/gohypergiant/AutoDC/code-of-conduct.md) before contributing to this project.

### Creating a pull request (PR)

1. Fork the Github repository at https://github.com/gohypergiant/AutoDC.
2. Clone your fork, create a new branch, push commits to the branch.
3. Consider whether documentation or tests need to be added or updated as part of the change, and add them as needed.
4. Open a pull request against the master branch of gohypergiant/AutoDC. Only in special cases would the PR be opened against other branches.
5. The PR title should describe the proposed change in the PR itself.
	* Follow [The 7 rules for a great commit message]((http://chris.beams.io/posts/git-commit/))
	* Separate subject from body with a blank line
	* Limit the subject line to 50 characters
	* Capitalize the subject line
	* Do not end the subject line with a period
	* Use the imperative mood in the subject line
	* Wrap the body at 72 characters
	* Use the body to explain what and why vs. how

### Review process

The review process can help the project achieve a high-quality code base. When performing code reviews, various aspects should be 
considered, and this code review checklist gives some examples of such items.

What to expect from the review process?

* Other reviewers, including committers, may comment on the changes and suggest modifications. Changes can be added by simply pushing more commits to the same branch.
* Lively, polite, rapid technical debate is encouraged from everyone in the community.
* AutoDC uses the LGTM convention for indicating the strongest level of technical sign-off on a patch: simply comment with the word "LGTM". It specifically means: "I've looked at this thoroughly and take as much ownership as if I wrote the patch myself". If you comment LGTM you will be expected to help with bugs or follow-up issues on the patch. Consistent, judicious use of LGTMs is a great way to gain credibility as a reviewer with the broader community.
* Sometimes, other changes will be merged which conflict with your pull request's changes. The PR can't be merged until the conflict is resolved. This can be resolved with "git fetch origin" followed by "git merge origin/master" and resolving the conflicts by hand, then pushing the result to your branch.
* Try to be responsive to the discussion rather than let days pass between replies.
