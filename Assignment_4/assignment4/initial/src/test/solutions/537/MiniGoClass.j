.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is p LPerson; from Label2 to Label3
	new Person
	dup
	invokespecial Person/<init>()V
	astore_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	new String_MiniGo
	dup
	ldc "John"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield Person/name LString_MiniGo;
	dup
	bipush 30
	putfield Person/age I
	dup
	iconst_2
	anewarray Car
	dup
	iconst_0
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
	aastore
	dup
	iconst_1
	new Car
	dup
	invokespecial Car/<init>()V
	dup
	new String_MiniGo
	dup
	ldc "Honda"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield Car/name LString_MiniGo;
	dup
	sipush 2021
	putfield Car/year I
	aastore
	putfield Person/cars [LCar;
	astore_1
	aload_1
	invokevirtual Person/print()V
	aload_1
	invokevirtual Person/changed()V
	aload_1
	invokevirtual Person/print()V
.var 2 is bot LAI; from Label2 to Label3
	aload_1
	astore_2
.var 3 is car LCar; from Label2 to Label3
	aload_2
	invokeinterface AI/getCar()LCar; 1
	astore_3
	aload_3
	invokevirtual Car/print()V
	aload_3
	invokevirtual Car/changed()V
	aload_3
	invokevirtual Car/print()V
	aload_2
	invokeinterface AI/getCar()LCar; 1
	invokevirtual Car/print()V
Label3:
Label1:
	return
.limit stack 15
.limit locals 4
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
