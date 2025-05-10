.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static initA(IZLString_MiniGo;)LA;
.var 0 is x I from Label0 to Label1
.var 1 is z Z from Label0 to Label1
.var 2 is s LString_MiniGo; from Label0 to Label1
Label0:
Label2:
	new A
	dup
	invokespecial A/<init>()V
	dup
	iload_0
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	dup
	iload_1
	putfield A/z Z
	dup
	aload_2
	putfield A/s LString_MiniGo;
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	astore_1
	iconst_1
	iconst_1
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/initA(IZLString_MiniGo;)LA;
	astore_1
	aload_1
	invokevirtual A/foo()V
	aload_1
	iconst_5
	invokevirtual A/initarr(I)V
	aload_1
	invokevirtual A/printArr()V
	aload_1
	invokevirtual A/initB()V
	aload_1
	invokevirtual A/testB()V
Label3:
Label1:
	return
.limit stack 8
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
