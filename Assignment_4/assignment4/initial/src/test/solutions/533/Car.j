.source Car.java
.class public Car
.super java/lang/Object
.field name LString_MiniGo;
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

.method public init(LString_MiniGo;I)LCar;
.var 0 is this LCar; from Label0 to Label1
.var 1 is name LString_MiniGo; from Label0 to Label1
.var 2 is year I from Label0 to Label1
Label0:
Label2:
	new Car
	dup
	invokespecial Car/<init>()V
	dup
	aload_1
	putfield Car/name LString_MiniGo;
	dup
	iload_2
	putfield Car/year I
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method

.method public print()V
.var 0 is this LCar; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Car/name LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
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
 	getfield Car/name LString_MiniGo;

	new String_MiniGo
	dup
	ldc "Honda"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V

	invokevirtual String_MiniGo/getValue()Ljava/lang/String;

	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V

	aload_0
	sipush 2021

	putfield Car/year I
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method
