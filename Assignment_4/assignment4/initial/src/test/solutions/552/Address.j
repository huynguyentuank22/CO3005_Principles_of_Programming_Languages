.source Address.java
.class public Address
.super java.lang.Object
.field public street Ljava/lang/String;
.field public city Ljava/lang/String;

.method public <init>(Ljava/lang/String;Ljava/lang/String;)V
Label0:
.var 0 is this LAddress; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is street Ljava/lang/String; from Label0 to Label1
.var 2 is city Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Address/street Ljava/lang/String;
	aload_0
	aload_2
	putfield Address/city Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LAddress; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	ldc ""
	putfield Address/street Ljava/lang/String;
	aload_0
	ldc ""
	putfield Address/city Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method
