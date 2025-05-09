.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I
.field static a [LGoString;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a1 [LGoString; from Label2 to Label3
	getstatic MiniGoClass/MAX I
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "cc"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "zz"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	astore_1
	getstatic MiniGoClass/a [LGoString;
	iconst_1
	aaload
	invokestatic MiniGoClass/foo(LGoString;)V
	aload_1
	iconst_0
	aaload
	invokestatic MiniGoClass/foo(LGoString;)V
	aload_1
	iconst_1
	aaload
	invokestatic MiniGoClass/foo(LGoString;)V
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
	getstatic MiniGoClass/a [LGoString;
	iload_2
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iload_2
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label13:
	goto Label4
Label5:
Label7:
.var 3 is str LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "xx"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	astore_3
	aload_3
	invokestatic MiniGoClass/foo(LGoString;)V
	aload_3
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 15
.limit locals 4
.end method

.method public static foo(LGoString;)V
.var 0 is s LGoString; from Label0 to Label1
Label0:
Label2:
	aload_0
	new GoString
	dup
	ldc "uu"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/compare(LGoString;)I
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	aload_0
	aload_0
	new GoString
	dup
	ldc "passbyref"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
Label10:
	goto Label7
Label6:
Label11:
Label12:
	aload_0
	new GoString
	dup
	ldc "pass"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
Label13:
Label7:
Label3:
Label1:
	return
.limit stack 10
.limit locals 1
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
	iconst_2
	putstatic MiniGoClass/MAX I
	getstatic MiniGoClass/MAX I
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "aa"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "bb"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	putstatic MiniGoClass/a [LGoString;
Label0:
Label1:
	return
.limit stack 8
.limit locals 0
.end method
