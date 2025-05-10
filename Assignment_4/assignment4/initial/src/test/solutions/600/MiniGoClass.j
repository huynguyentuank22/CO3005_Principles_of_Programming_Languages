.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static maxInMatrix([[I)I
.var 0 is matrix [[I from Label0 to Label1
Label0:
Label2:
.var 1 is max I from Label2 to Label3
	aload_0
	iconst_0
	aaload
	iconst_0
	iaload
	istore_1
Label6:
.var 2 is i I from Label6 to Label7
	iconst_0
	istore_2
Label8:
	iload_2
	iconst_2
	if_icmpge Label10
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
Label16:
.var 3 is j I from Label16 to Label17
	iconst_0
	istore_3
Label18:
	iload_3
	iconst_2
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label15
	goto Label19
Label14:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label18
Label19:
Label22:
	aload_0
	iload_2
	aaload
	iload_3
	iaload
	iload_1
	if_icmple Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label26
Label28:
Label29:
	aload_0
	iload_2
	aaload
	iload_3
	iaload
	istore_1
Label30:
Label26:
Label27:
Label23:
	goto Label14
Label15:
Label17:
Label13:
	goto Label4
Label5:
Label7:
	iload_1
	ireturn
Label3:
Label1:
.limit stack 18
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is matrix [[I from Label2 to Label3
	iconst_2
	iconst_2
	multianewarray [[I 2
	dup
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
	astore_1
	aload_1
	invokestatic MiniGoClass/maxInMatrix([[I)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 18
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
