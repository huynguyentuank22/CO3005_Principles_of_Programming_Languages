.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static getArr()[LPerson;
Label0:
Label2:
	iconst_2
	anewarray Person
	dup
	iconst_0
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
	aastore
	dup
	iconst_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	new String_MiniGo
	dup
	ldc "Jane"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield Person/name LString_MiniGo;
	dup
	bipush 25
	putfield Person/age I
	aastore
	areturn
Label3:
Label1:
.limit stack 10
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [LPerson; from Label2 to Label3
	iconst_2
	anewarray Person
	astore_1
	invokestatic MiniGoClass/getArr()[LPerson;
	astore_1
	aload_1
	iconst_0
	aaload
	invokevirtual Person/print()V
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
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
