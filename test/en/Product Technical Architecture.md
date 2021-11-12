### 1 Product Technical Architecture
Chain33 is designed with a plug-in architecture, retaining only the core functionality and adding extensions as plug-ins.
Plugin-based design has many benefits. It can separate the extended functions from the system framework, reduce the complexity of the framework and make it easier to implement.  
The extended functionality is associated with the system framework in a loosely coupled manner, and both can evolve and be published independently while maintaining the same interfaces.

Chain33 plug-in architecture is shown below:  

![插件架构图](https://public.33.cn/web/storage/upload/20181114/b7baad80b9c4cbe18bb964d0a9024acf.png)
