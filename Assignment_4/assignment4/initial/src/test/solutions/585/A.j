.source A.java
.class public A
.super java/lang/Object
.implements B
.field s LGoString;

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public setS(LGoString;)V
.var 0 is this LA; from Label0 to Label1
.var 1 is s LGoString; from Label0 to Label1
Label0:
Label2:
	aload_0
 	getfield A/s LGoString;

	aload_1

	invokevirtual GoString/getValue()Ljava/lang/String;

	invokevirtual GoString/setValue(Ljava/lang/String;)V

Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public getS()LGoString;
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/s LGoString;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
