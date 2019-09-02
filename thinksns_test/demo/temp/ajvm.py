import jpype
# jvm_path = r"C:\Program Files\Java\jdk1.8.0_151\jre\bin\server\jvm.dll"
jvm_path = jpype.getDefaultJVMPath()
jpype.startJVM(jvm_path)
jpype.isJVMStarted()

jpype.java.lang.System.out.println("hello world")

jpype.shutdownJVM()