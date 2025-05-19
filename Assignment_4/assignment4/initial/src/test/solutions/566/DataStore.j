.source DataStore.java
.class public DataStore
.super java.lang.Object
.implements Storage
.field public entries [Ljava/lang/String;

.method public <init>([Ljava/lang/String;)V
Label0:
.var 0 is this LDataStore; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is entries [Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield DataStore/entries [Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
Label0:
.var 0 is this LDataStore; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public setEntries([Ljava/lang/String;)V
Label0:
.var 0 is this LDataStore; from Label0 to Label1
.var 1 is new_entries [Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield DataStore/entries [Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public getEntries()[Ljava/lang/String;
Label0:
.var 0 is this LDataStore; from Label0 to Label1
Label2:
	aload_0
	getfield DataStore/entries [Ljava/lang/String;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
