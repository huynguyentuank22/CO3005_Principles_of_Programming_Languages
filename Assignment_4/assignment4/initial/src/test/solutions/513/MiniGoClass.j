.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_5
	invokestatic io/putInt(I)V
	iconst_5
	invokestatic io/putIntLn(I)V
	ldc 5.0
	invokestatic io/putFloat(F)V
	ldc 5.0
	invokestatic io/putFloatLn(F)V
	iconst_1
	invokestatic io/putBool(Z)V
	iconst_0
	invokestatic io/putBoolLn(Z)V
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	new GoString
	dup
	ldc "World"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic io/putLn()V
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
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
