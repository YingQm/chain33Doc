# Chain33 Parallel Chain Upgrade Regulation
[TOC]

## 1 Scenario
When the Chain33 parallel chain is staged developed and ready for external release. Includes small release (6.2.x), large release (6.3.0)

## 2 Background of Specification Development
Chain33 parallel chain function iterates and uses more and more project parties. We need to standardize and streamline the upgrade work, and do the work at ordinary times to reduce the pressure of the upgrade process.

## 3 Chain33 Parallel Chain Version Upgrade Reason
Chain33 upgrades are usually based on the following reasons:
1）.  There are bugs in the existing version. Use upgrades to fix bugs.
2）.  Optimize the performance and efficiency of the existing version. For example, 6.1 to 6.2 optimize storage efficiency.
3）.  The existing version can not meet the needs of users, some new features need to be added.
4）.  Chain33 team tracks new technologies in the industry and independently develops new features of blockchain.

## 4 How Do We Do Upgrade Normalization
Chain33 development, testing, product, operation and maintenance are required to standardize the upgrade work based on the current configuration of company personnel.

#### 4.1. Chain33 Development and Research
###### Development stage
1）. Any code change needs to submit the corresponding issue, title and content on github as detailed as possible, so as to quickly backtrack in the future.

2）. It is recommended to place a parallel chain configuration file in the plugin directory. If any parameter changes occur during development, this file should be modified simultaneously.

3）. Developers need to specify the newly introduced fork configuration item and parameter configuration item. Take the ForkBase58AddressCheck change as an example:
> Add change record at the top of the parallel chain configuration file: add ForkBase58AddressCheck configuration item under[fork.system]TAB, xx, xx, 2019.
> Add a clear note above the ForkBase58AddressCheck configuration item: what problem to solve, configuration recommendations.

4）. After the function development is completed and the self-test is passed, submit the merge request.

###### Code check-in
Chain33 product owner extracts all or part of functionality to form a release (such as release6.2.1) based on bugs and requirements, and testers intervene.

In principle, this version will no longer incorporate any extraneous code without special requirements. Including the problems found and modified in the test process, which only accept the integration of relevant functions.

#### 4.2. Chain33 Testers
1）.  Verify the basic functionality of the release.

2）.  As for the upgrade of the verification version, it is recommended to gradually improve a test library that contains configuration files of several different project parties, and try to include full-service contracts (coins contract, token contract, game contract, etc.). 

3）.  The upgrade process covers both smooth upgrade and new upgrade scenarios to ensure consistent state hashes before and after the upgrade.

4) .  After verification, package the upgraded version and upload it to the oss server and output the upgrade document. 
> The upgrade document contains: upgrade reason; new configuration parameters, fork parameter description and suggested configuration; version download path; detailed upgrade steps; status check before and after upgrade.

#### 4.3. Marketing/Product People
Make an appointment with the project party in advance about the upgrade time and reason, and collect corresponding feedback.

#### 4.4. Operation and Maintenance
1）. Ensure that the version obtained is consistent with the upgrade documentation.
2）. Follow the upgrade document steps strictly, pay special attention to the height of fork, each chain configuration is different, which need to be independently configured by the operation and maintenance people in the upgrade process.
3）. After the upgrade, do pre and post status checks according to the upgrade documentation. Find out the inconsistent state, feedback to R&R in time.
