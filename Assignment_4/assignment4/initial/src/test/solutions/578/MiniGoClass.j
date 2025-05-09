.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static callCount I

.method public static factorial(I)I
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/callCount I
	iconst_1
	iadd
	putstatic MiniGoClass/callCount I
	iload_0
	iconst_1
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	iconst_1
	ireturn
Label10:
Label6:
Label7:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MiniGoClass/factorial(I)I
	imul
	ireturn
Label3:
Label1:
.limit stack 10
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_0
	dup
	ifle Label6
	pop
	iconst_5
	invokestatic MiniGoClass/factorial(I)I
	bipush 10
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
Label6:
	ifle Label7
Label9:
Label10:
	new GoString
	dup
	ldc "Won't print"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label11:
Label7:
Label8:
	getstatic MiniGoClass/callCount I
	invokestatic io/putIntLn(I)V
	iconst_1
	dup
	ifgt Label14
	pop
	iconst_5
	invokestatic MiniGoClass/factorial(I)I
	bipush 10
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
Label14:
	ifle Label15
Label17:
Label18:
	new GoString
	dup
	ldc "Short-circuited"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label19:
Label15:
Label16:
	getstatic MiniGoClass/callCount I
	invokestatic io/putIntLn(I)V
.var 1 is result I from Label2 to Label3
	iconst_5
	invokestatic MiniGoClass/factorial(I)I
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/callCount I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label20:
Label21:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	iconst_0
	putstatic MiniGoClass/callCount I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
