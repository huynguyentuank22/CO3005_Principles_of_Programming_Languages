.source Archive.java
.class public Archive
.super java.lang.Object
.field public id Ljava/lang/String;
.field public items [Ljava/lang/String;

.method public <init>(Ljava/lang/String;[Ljava/lang/String;)V
Label0:
.var 0 is this LArchive; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is id Ljava/lang/String; from Label0 to Label1
.var 2 is items [Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Archive/id Ljava/lang/String;
	aload_0
	aload_2
	putfield Archive/items [Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LArchive; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public listItems()V
Label0:
.var 0 is this LArchive; from Label0 to Label1
Label2:
.var 1 is i I from Label2 to Label3
	iconst_0
	istore_1
	iload_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
Label9:
	aload_0
	getfield Archive/items [Ljava/lang/String;
	iload_1
	aaload
	ldc ""
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	iconst_0
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label15:
	ldc "Item: "
	aload_0
	getfield Archive/items [Ljava/lang/String;
	iload_1
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label16:
	goto Label14
Label11:
Label14:
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_2
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label5
	goto Label8
Label5:
Label19:
Label3:
Label1:
	return
.limit stack 12
.limit locals 2
.end method
