package Database;
use DBI;
use strict;

my $dbh;
getDbh();

sub getDbh {
	my ( $args ) = @_;
	my $db = $args->{db} || 'ecomm';
	my $dsn = "DBI:mysql:database=$db";
	my $uname = $args->{username} || 'root';
	my $pass = $args->{password} || 'manager';
	$dbh = DBI->connect($dsn, $uname, $pass ,  {InactiveDestroy => 1, RaiseError => 1, PrintError => 1});
}

# sub select {
	# my ( $args ) = @_;
	# my $fields = $args->{fields} || '*';
	# my $table = $args->{table};
	# my $where = $args->{where} || '';
	
	# my $query = "SELECT $fields from $table";
	# $query .= "where ";
	# my $sth = $dbh->prepare("SELECT FIRST_NAME, LAST_NAME
                        # FROM TEST_TABLE
                        # WHERE AGE > ?");
# }

sub exec_query{
	my ( $args ) = @_;
	my $query = $args->{query};
	my $sth = $dbh->prepare($query);
	 eval {
    
    $sth->execute();
    
  };
  if ($@) {
    # $sth->err and $DBI::err will be true if error was from DBI
    warn $@; # print the error
  }
	
	$sth->finish();
	# $dbh->commit;
	return $sth->fetchall_arrayref if $query =~ /^\s*select/i;
	return $sth->rows;
}

END {
	$dbh->disconnect  or warn $dbh->errstr;
}
1;