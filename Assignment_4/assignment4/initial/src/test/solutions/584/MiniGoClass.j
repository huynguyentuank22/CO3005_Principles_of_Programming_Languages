.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static complex(LA;[LGoString;LB;)V
.var 0 is a LA; from Label0 to Label1
.var 1 is arr [LGoString; from Label0 to Label1
.var 2 is b LB; from Label0 to Label1
Label0:
Label2:
	aload_0
	invokevirtual A/getS()LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	invokeinterface B/getS()LGoString; 1
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	new A
	dup
	invokespecial A/<init>()V
	dup
	new GoString
	dup
	ldc ""
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putfield A/s LGoString;
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
	new A
	dup
	invokespecial A/<init>()V
	dup
	new GoString
	dup
	ldc "uu"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putfield A/s LGoString;
	invokestatic MiniGoClass/complex(LA;[LGoString;LB;)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 1
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
