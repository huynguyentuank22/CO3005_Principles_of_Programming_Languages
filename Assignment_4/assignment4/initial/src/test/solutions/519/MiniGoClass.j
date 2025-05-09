.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a Z from Label2 to Label3
	iconst_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
.var 2 is b Z from Label2 to Label3
	iconst_0
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	istore_2
	iload_2
	invokestatic io/putBoolLn(Z)V
.var 3 is c Z from Label2 to Label3
	iload_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
.var 4 is d Z from Label2 to Label3
	iload_2
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	istore 4
	iload 4
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 13
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label12:
Label13:
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
