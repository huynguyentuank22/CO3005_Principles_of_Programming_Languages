.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static genStr(LGoString;)LGoString;
.var 0 is v LGoString; from Label0 to Label1
Label0:
Label2:
	aload_0
	new GoString
	dup
	ldc "aa"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	new GoString
	dup
	ldc "bc"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	areturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [LGoString; from Label2 to Label3
	getstatic MiniGoClass/MAX I
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "pp"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "cc"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	astore_1
.var 2 is b LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "jj"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/genStr(LGoString;)LGoString;
	astore_2
.var 3 is c LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "ii"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/genStr(LGoString;)LGoString;
	astore_3
Label3:
Label1:
	return
.limit stack 7
.limit locals 4
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
	iconst_2
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
