.source Student.java
.class public Student
.super java.lang.Object
.field public id Ljava/lang/String;
.field public grade I

.method public <init>(Ljava/lang/String;I)V
Label0:
.var 0 is this LStudent; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is id Ljava/lang/String; from Label0 to Label1
.var 2 is grade I from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Student/id Ljava/lang/String;
	aload_0
	iload_2
	putfield Student/grade I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LStudent; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public printDetails()V
Label0:
.var 0 is this LStudent; from Label0 to Label1
Label2:
	ldc "ID: "
	aload_0
	getfield Student/id Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Student/grade I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
