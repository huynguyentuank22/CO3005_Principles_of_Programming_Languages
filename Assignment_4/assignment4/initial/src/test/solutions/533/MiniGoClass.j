.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static init(LString_MiniGo;IFLCar;)LPerson;
.var 0 is name LString_MiniGo; from Label0 to Label1
.var 1 is age I from Label0 to Label1
.var 2 is height F from Label0 to Label1
.var 3 is car LCar; from Label0 to Label1
Label0:
Label2:
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	aload_0
	putfield Person/name LString_MiniGo;
	dup
	iload_1
	putfield Person/age I
	dup
	fload_2
	putfield Person/height F
	dup
	aload_3
	putfield Person/car LCar;
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is car LCar; from Label2 to Label3
	new Car
	dup
	invokespecial Car/<init>()V
	dup
	new String_MiniGo
	dup
	ldc "Toyota"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield Car/name LString_MiniGo;
	dup
	sipush 2020
	putfield Car/year I
	astore_1
	aload_1
	invokevirtual Car/print()V
	aload_1
	invokevirtual Car/changed()V
	aload_1
	invokevirtual Car/print()V
.var 2 is x LPerson; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "John"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	bipush 30
	ldc 177.3
	aload_1
	invokestatic MiniGoClass/init(LString_MiniGo;IFLCar;)LPerson;
	astore_2
	aload_2
	invokevirtual Person/bar()V
Label3:
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label4:
Label5:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
