.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is myLib LLibrary; from Label2 to Label3
	new Library
	dup
	invokespecial Library/<init>()V
	dup
	new GoString
	dup
	ldc "Central Library"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putfield Library/name LGoString;
	dup
	iconst_3
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "Go Programming"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "Python Basics"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_2
	new GoString
	dup
	ldc ""
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	putfield Library/books [LGoString;
	astore_1
	aload_1
	invokevirtual Library/printBooks()V
Label3:
Label1:
	return
.limit stack 11
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
