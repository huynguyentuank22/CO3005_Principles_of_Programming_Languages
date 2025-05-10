.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is sum I from Label2 to Label3
	iconst_0
	istore_1
Label6:
.var 2 is i I from Label6 to Label7
	iconst_1
	istore_2
Label8:
	iload_2
	bipush 10
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
Label12:
	iload_2
	iconst_3
	irem
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	iload_2
	iconst_5
	irem
	iconst_0
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ior
	ifle Label18
Label20:
Label21:
	iload_1
	iload_2
	iadd
	istore_1
Label22:
Label18:
Label19:
Label13:
	goto Label4
Label5:
Label7:
	iload_1
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 17
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label23:
Label24:
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
