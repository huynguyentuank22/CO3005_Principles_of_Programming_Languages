.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_0
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	astore_1
	aload_1
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual A/main(LGoString;)V
Label3:
Label1:
	return
.limit stack 4
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
