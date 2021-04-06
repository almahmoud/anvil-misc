# Automated Tests for Galaxy on Kubernetes Stacks
## Galaxy on GKE deployed via GalaxyKubeMan (AnVIL)
### Deployment Testing
Twice a day, [GalaxyKubeMan (GKM)](https://github.com/galaxyproject/galaxykubeman-helm) is deployed on GKE, mimicking an AnVIL deployment. The purpose of these tests is to provide reasonable confidence that Galaxy is launchable on the AnVIL everyday.

Below is a plot summarizing successful deployments and GKM install times.
<a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/deployments.html">Click here</a> or on the image for more details.

<a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/deployments.html"><img src="reports/anvil/deployments.svg" /></a>

### Tool Testing
After each successful deployment, automated tool tests are also run against the instance. These serve as an end-to-end-like test for Galaxy, providing confidence that Galaxy is not only launchable but functional. These tests cycle on a weekly basis through the entire suite of tools installed by default on AnVIL, providing reasonable confidence that the tools encountered by most users remain functional, and automating the detection and reporting of tools breaking.

Latest tool tests for each chunk:


[April 05 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-05-21-02-00/results.html)
[April 05 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-05-15-03-31/results.html)


[April 05 09:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-05-09-02-44/results.html)
[April 05 03:07](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-05-03-07-38/results.html)


[April 04 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-04-21-02-13/results.html)
[April 04 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-04-15-03-32/results.html)


[April 04 09:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-04-09-02-21/results.html)


[April 03 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-03-21-02-05/results.html)
[April 03 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-03-15-03-33/results.html)


[April 03 09:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-03-09-02-32/results.html)
[April 03 03:06](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-03-03-06-15/results.html)


[April 02 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-02-21-02-08/results.html)
[April 02 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-02-15-03-37/results.html)


[April 02 09:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-02-09-03-26/results.html)
[April 02 03:08](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-02-03-08-14/results.html)


[April 01 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-01-21-02-20/results.html)
[April 01 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-01-15-03-28/results.html)


[April 01 09:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-01-09-03-10/results.html)
[April 01 03:07](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-01-03-07-59/results.html)


[March 31 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-31-21-02-21/results.html)
[March 31 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-31-15-03-45/results.html)


[March 31 09:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-31-09-02-32/results.html)
[March 31 03:06](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-31-03-06-05/results.html)


[March 30 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-30-21-02-06/results.html)
[March 30 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-30-15-03-41/results.html)


[March 30 09:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-30-09-02-37/results.html)
[March 30 03:05](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-30-03-05-58/results.html)


[March 29 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-29-21-02-03/results.html)
[March 29 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-29-15-03-52/results.html)


[March 29 09:06](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-29-09-06-13/results.html)
[March 29 03:08](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-29-03-08-42/results.html)


[March 28 21:02](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-28-21-02-07/results.html)
[March 28 15:03](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-28-15-03-23/results.html)


[March 27 09:53](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-27-09-53-25/results.html)
[March 27 03:55](https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-03-27-03-55-30/results.html)
