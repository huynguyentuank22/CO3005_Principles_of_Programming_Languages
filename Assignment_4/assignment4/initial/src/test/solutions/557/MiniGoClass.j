.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[I from Label2 to Label3
	getstatic MiniGoClass/MAX I
	getstatic MiniGoClass/MAX I
	multianewarray [[I 2
	astore_1
	getstatic MiniGoClass/MAX I
	getstatic MiniGoClass/MAX I
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
	iconst_0
	aaload
	iconst_2
	iconst_3
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_5
	iastore
	dup
	iconst_1
	aaload
	iconst_2
	bipush 6
	iastore
	dup
	iconst_2
	aaload
	iconst_0
	bipush 7
	iastore
	dup
	iconst_2
	aaload
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	aaload
	iconst_2
	bipush 9
	iastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	aload_1
	iconst_0
	aaload
	iconst_0
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	iconst_2
	iadd
	iastore
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	aload_1
	iconst_1
	aaload
	iconst_1
	aload_1
	iconst_1
	aaload
	iconst_1
	iaload
	iconst_3
	iadd
	iastore
	aload_1
	iconst_2
	aaload
	iconst_2
	aload_1
	iconst_2
	aaload
	iconst_2
	iaload
	iconst_4
	iadd
	iastore
Label6:
.var 2 is i I from Label6 to Label7
	iconst_0
	istore_2
Label8:
	iload_2
	getstatic MiniGoClass/MAX I
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
	getstatic MiniGoClass/MAX I
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
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/putInt(I)V
Label23:
	goto Label14
Label15:
Label17:
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 108
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label24:
Label25:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	iconst_3
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
