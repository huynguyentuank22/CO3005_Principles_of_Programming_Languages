.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static power(II)I
.var 0 is base I from Label0 to Label1
.var 1 is exp I from Label0 to Label1
Label0:
Label2:
.var 2 is result I from Label2 to Label3
	iconst_1
	istore_2
Label6:
.var 3 is i I from Label6 to Label7
	iconst_0
	istore_3
Label8:
	iload_3
	iload_1
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label8
Label9:
Label12:
	iload_2
	iload_0
	imul
	istore_2
Label13:
	goto Label4
Label5:
Label7:
	iload_2
	ireturn
Label3:
Label1:
.limit stack 8
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	iconst_2
	iconst_3
	invokestatic MiniGoClass/power(II)I
	istore_1
.var 2 is b I from Label2 to Label3
	iconst_3
	iconst_2
	invokestatic MiniGoClass/power(II)I
	istore_2
	iload_1
	iload_2
	iadd
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 6
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
