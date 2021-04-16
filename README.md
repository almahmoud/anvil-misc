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

<table id="anviltools"><thead><tr><th>Chunk ID</th><th>Tool List</th><th>Latest report</th><th>Previous report</th></tr></thead><tbody><tr><td>0</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-12-03-08-47/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-12-03-08-47/results.html">Mon Apr 12 03:20:57 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>1</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-12-15-05-28/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-12-15-05-28/results.html">Mon Apr 12 15:17:22 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>2</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-13-03-09-06/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-13-03-09-06/results.html">Tue Apr 13 03:20:29 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>3</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-13-15-03-40/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-13-15-03-40/results.html">Tue Apr 13 15:16:08 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>4</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-14-03-05-41/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-14-03-05-41/results.html">Wed Apr 14 03:17:10 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>5</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-14-15-03-47/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-14-15-03-47/results.html">Wed Apr 14 15:19:52 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-08-24-47/results.html">Thu Apr 08 08:38:36 2021</a></td></tr><tr><td>6</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-15-03-04-50/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-15-03-04-50/results.html">Thu Apr 15 03:19:26 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-14-20-09-02/results.html">Wed Apr 14 20:21:27 2021</a></td></tr><tr><td>7</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-15-15-03-34/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-15-15-03-34/results.html">Thu Apr 15 15:19:44 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-15-03-39/results.html">Thu Apr 08 15:15:27 2021</a></td></tr><tr><td>8</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-16-03-08-27/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-16-03-08-27/results.html">Fri Apr 16 03:23:21 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-09-03-03-47/results.html">Fri Apr 09 03:15:37 2021</a></td></tr><tr><td>9</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-16-15-03-47/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-16-15-03-47/results.html">Fri Apr 16 15:21:55 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-09-15-03-32/results.html">Fri Apr 09 15:17:28 2021</a></td></tr><tr><td>10</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-10-03-06-22/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-10-03-06-22/results.html">Sat Apr 10 03:19:28 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-03-50-28/results.html">Thu Apr 08 04:01:55 2021</a></td></tr><tr><td>11</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-10-15-03-42/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-10-15-03-42/results.html">Sat Apr 10 15:15:56 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-00-42-57/results.html">Thu Apr 08 00:55:18 2021</a></td></tr><tr><td>12</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-00-19-13/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-08-00-19-13/results.html">Thu Apr 08 00:30:56 2021</a></td><td><a href="N/A">N/A</a></td></tr><tr><td>13</td><td><a href="https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-11-15-03-35/tools.yaml">Toolset</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-11-15-03-35/results.html">Sun Apr 11 15:16:47 2021</a></td><td><a href="https://htmlpreview.github.io/?https://github.com/almahmoud/anvil-misc/blob/master/reports/anvil/tool-tests/gxy-auto-04-07-23-23-53/results.html">Wed Apr 07 23:35:51 2021</a></td></tr></tbody></table>
