.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a Z from Label2 to Label3
	iconst_1
	dup
	ifle Label5
	pop
	iconst_0
Label5:
	dup
	ifgt Label4
	pop
	iconst_1
Label4:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
.var 2 is b Z from Label2 to Label3
	iconst_0
	dup
	ifgt Label6
	pop
	iconst_1
	dup
	ifle Label7
	pop
	iconst_0
Label7:
Label6:
	istore_2
	iload_2
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label8:
Label9:
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
