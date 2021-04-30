# Automated Tests for Galaxy on Kubernetes Stacks
## Galaxy on GKE deployed via GalaxyKubeMan (AnVIL)
### Deployment Testing
Twice a day, [GalaxyKubeMan (GKM)](https://github.com/galaxyproject/galaxykubeman-helm) is deployed on GKE, mimicking an AnVIL deployment. The purpose of these tests is to provide reasonable confidence that Galaxy is launchable on the AnVIL everyday.

Below is a plot summarizing successful deployments and GKM install times.
<a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/deployments.html">Click here</a> or on the image for more details.

<a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/deployments.html"><img src="deployments.svg" /></a>

### Tool Testing
After each successful deployment, automated tool tests are also run against the instance. These serve as an end-to-end-like test for Galaxy, providing confidence that Galaxy is not only launchable but functional. These tests cycle on a weekly basis through the entire suite of tools installed by default on AnVIL, providing reasonable confidence that the tools encountered by most users remain functional, and automating the detection and reporting of tools breaking.

Latest tool tests for each chunk:

<table id="anviltools"><thead><tr><th>Chunk ID</th><th>Tool List</th><th>Latest report</th><th>Previous report</th></tr></thead><tbody><tr><td>0</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-26-09-06-38/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-26-09-06-38/results.html">Mon Apr 26 09:19:56 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-26-03-11-07/results.html">Mon Apr 26 03:25:00 2021</a></td></tr><tr><td>1</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-26-21-04-39/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-26-21-04-39/results.html">Mon Apr 26 21:16:09 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-26-15-02-11/results.html">Mon Apr 26 15:15:51 2021</a></td></tr><tr><td>2</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-27-09-06-19/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-27-09-06-19/results.html">Tue Apr 27 09:17:53 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-27-03-07-56/results.html">Tue Apr 27 03:19:29 2021</a></td></tr><tr><td>3</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-27-21-04-29/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-27-21-04-29/results.html">Tue Apr 27 21:16:16 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-27-15-02-03/results.html">Tue Apr 27 15:15:16 2021</a></td></tr><tr><td>4</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-28-09-06-25/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-28-09-06-25/results.html">Wed Apr 28 09:17:23 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-28-03-09-38/results.html">Wed Apr 28 03:22:39 2021</a></td></tr><tr><td>5</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-28-21-04-34/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-28-21-04-34/results.html">Wed Apr 28 21:17:51 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-28-15-02-09/results.html">Wed Apr 28 15:14:26 2021</a></td></tr><tr><td>6</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-29-09-05-57/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-29-09-05-57/results.html">Thu Apr 29 09:17:38 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-29-03-05-27/results.html">Thu Apr 29 03:17:15 2021</a></td></tr><tr><td>7</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-29-21-04-19/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-29-21-04-19/results.html">Thu Apr 29 21:17:46 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-29-15-02-02/results.html">Thu Apr 29 15:15:50 2021</a></td></tr><tr><td>8</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-30-03-21-06/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-30-03-21-06/results.html">Fri Apr 30 03:32:36 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-23-09-06-53/results.html">Fri Apr 23 09:22:23 2021</a></td></tr><tr><td>9</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-23-21-04-38/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-23-21-04-38/results.html">Fri Apr 23 21:18:01 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-23-15-02-11/results.html">Fri Apr 23 15:14:24 2021</a></td></tr><tr><td>10</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-24-09-06-08/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-24-09-06-08/results.html">Sat Apr 24 09:18:23 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-24-03-09-01/results.html">Sat Apr 24 03:20:46 2021</a></td></tr><tr><td>11</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-24-21-04-31/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-24-21-04-31/results.html">Sat Apr 24 21:16:00 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-24-15-02-19/results.html">Sat Apr 24 15:13:23 2021</a></td></tr><tr><td>12</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-00-19-13/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-00-19-13/results.html">Thu Apr 08 00:30:56 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>13</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-25-21-04-41/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-25-21-04-41/results.html">Sun Apr 25 21:17:34 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-25-15-02-10/results.html">Sun Apr 25 15:15:05 2021</a></td></tr></tbody></table>
