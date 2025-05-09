.source Car.java
.class public Car
.super java/lang/Object
.field name LGoString;
.field year I

.method public <init>()V
.var 0 is this LCar; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public print()V
.var 0 is this LCar; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Car/name LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Car/year I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public changed()V
.var 0 is this LCar; from Label0 to Label1
Label0:
Label2:
	aload_0
 	getfield Car/name LGoString;

	new GoString
	dup
	ldc "Honda"
	invokespecial GoString/<init>(Ljava/lang/String;)V

	invokevirtual GoString/getValue()Ljava/lang/String;

	invokevirtual GoString/setValue(Ljava/lang/String;)V

	aload_0
	sipush 2019

	putfield Car/year I
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method
