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
	new String_MiniGo
	dup
	ldc "Central Library"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield Library/name LString_MiniGo;
	dup
	iconst_3
	anewarray String_MiniGo
	dup
	iconst_0
	new String_MiniGo
	dup
	ldc "Go Programming"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new String_MiniGo
	dup
	ldc "Python Basics"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_2
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	aastore
	putfield Library/books [LString_MiniGo;
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
