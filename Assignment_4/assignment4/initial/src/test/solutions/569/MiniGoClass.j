.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static arrsort([I)V
.var 0 is arr [I from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_0
	istore_1
Label8:
	iload_1
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
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label12:
Label16:
.var 2 is j I from Label16 to Label17
	iconst_0
	istore_2
Label18:
	iload_2
	iload_1
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label15
	goto Label19
Label14:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label18
Label19:
Label22:
	aload_0
	iload_1
	iaload
	aload_0
	iload_2
	iaload
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label26
Label28:
Label29:
.var 3 is temp I from Label29 to Label30
	aload_0
	iload_1
	iaload
	istore_3
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload_3
	iastore
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
Label3:
Label1:
	return
.limit stack 15
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is arr [I from Label2 to Label3
	getstatic MiniGoClass/MAX I
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	bipush 7
	iastore
	dup
	iconst_4
	bipush 8
	iastore
	dup
	iconst_5
	bipush 9
	iastore
	dup
	bipush 6
	bipush 12
	iastore
	dup
	bipush 7
	bipush 14
	iastore
	dup
	bipush 8
	bipush 15
	iastore
	dup
	bipush 9
	bipush 11
	iastore
	astore_1
	aload_1
	invokestatic MiniGoClass/arrsort([I)V
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
	aload_1
	iload_2
	iaload
	invokestatic io/putInt(I)V
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 37
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label14:
Label15:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	bipush 10
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
