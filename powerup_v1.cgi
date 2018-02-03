#!/usr/bin/perl -w

use CGI;
my $q = CGI->new();

my $REDforce = 0;
my $REDlevitate = 0;
my $REDboost = 0;
my $BLUEportal = 11;
my $REDrobot1 = 1;
my $REDrobot2 = 1;
my $REDrobot3 = 1;
my $pyramidL = 10;
my $REDswitchL = 0;
my $BLUEswitchL = 0;
my $switchL = 6;
my $REDscale = 0;
my $BLUEscale = 0;
my $switchR = 6;
my $REDswitchR = 0;
my $BLUEswitchR = 0;
my $pyramidR = 10;
my $BLUErobot1 = 1;
my $BLUErobot2 = 1;
my $BLUErobot3 = 1;
my $REDportal = 11;
my $BLUEforce = 0;
my $BLUElevitate = 0;
my $BLUEboost = 0;
my $stage = 0;
my $REDscore = 0;
my $BLUEscore = 0;
my $R1 = 0;
my $R2 = 0;
my $R3 = 0;
my $B1 = 0;
my $B2 = 0;
my $B3 = 0;
my $RC1 = 0;
my $RC2 = 0;
my $RC3 = 0;
my $BC1 = 0;
my $BC2 = 0;
my $BC3 = 0;


print "Content-type: text/html\n\n";
print "<html><head>\n";
print "<title>FIRST Power Up!</title>\n";
print "<link rel='SHORTCUT ICON' href='favicon.ico'>\n";
print "<link rel='apple-touch-icon' href='favicon.png'>\n";
print "<meta name='description' content='FIRST Robotics Team 1073, Power Up Strategy Game'>\n";
print "<meta name='keywords' content='FIRST, Robotics, 1073, The Force Team, Po\
wer Up, Strategy Game'>\n";
print "<meta name='author' content='FIRST Team 1073'>\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n";
print "</head>\n";
print "<body><center>\n";
print "<H1><I>FIRST</I> PowerUp! Strategy Game</H1>\n";

if ($q->param) {
    $REDforce = $q->param('REDforce') if (defined $q->param('REDforce'));
    $REDlevitate = $q->param('REDlevitate') if (defined $q->param('REDlevitate'));
    $REDboost = $q->param('REDboost') if (defined $q->param('REDboost'));
    $BLUEportal = $q->param('BLUEportal') if (defined $q->param('BLUEportal'));
    $BLUEportal = $q->param('BLUEportal') if (defined $q->param('BLUEportal'));
    $REDrobot1 = $q->param('REDrobot1') if (defined $q->param('REDrobot1'));
    $REDrobot2 = $q->param('REDrobot2') if (defined $q->param('REDrobot2'));
    $REDrobot3 = $q->param('REDrobot3') if (defined $q->param('REDrobot3'));
    $pyramidL = $q->param('pyramidL') if (defined $q->param('pyramidL'));
    $REDswitchL = $q->param('REDswitchL') if (defined $q->param('REDswitchL'));
    $BLUEswitchL = $q->param('BLUEswitchL') if (defined $q->param('BLUEswitchL'));
    $switchL = $q->param('switchL') if (defined $q->param('switchL'));
    $REDscale = $q->param('REDscale') if (defined $q->param('REDscale'));
    $BLUEscale = $q->param('BLUEscale') if (defined $q->param('BLUEscale'));
    $switchR = $q->param('switchR') if (defined $q->param('switchR'));
    $REDswitchR = $q->param('REDswitchR') if (defined $q->param('REDswitchR'));
    $BLUEswitchR = $q->param('BLUEswitchR') if (defined $q->param('BLUEswitchR'));
    $pyramidR = $q->param('pyramidR') if (defined $q->param('pyramidR'));
    $BLUErobot1 = $q->param('BLUErobot1') if (defined $q->param('BLUErobot1'));
    $BLUErobot2 = $q->param('BLUErobot2') if (defined $q->param('BLUErobot2'));
    $BLUErobot3 = $q->param('BLUErobot3') if (defined $q->param('BLUErobot3'));
    $REDportal = $q->param('REDportal') if (defined $q->param('REDportal'));
    $REDportal = $q->param('REDportal') if (defined $q->param('REDportal'));
    $BLUEforce = $q->param('BLUEforce') if (defined $q->param('BLUEforce'));
    $BLUElevitate = $q->param('BLUElevitate') if (defined $q->param('BLUElevitate'));
    $BLUEboost = $q->param('BLUEboost') if (defined $q->param('BLUEboost'));
    $stage = $q->param('stage') if (defined $q->param('stage'));
    $REDscore = $q->param('REDscore') if (defined $q->param('REDscore'));
    $BLUEscore = $q->param('BLUEscore') if (defined $q->param('BLUEscore'));
    $R1 = $q->param('R1') if (defined $q->param('R1'));
    $R2 = $q->param('R2') if (defined $q->param('R2'));
    $R3 = $q->param('R3') if (defined $q->param('R3'));
    $B1 = $q->param('B1') if (defined $q->param('B1'));
    $B2 = $q->param('B2') if (defined $q->param('B2'));
    $B3 = $q->param('B3') if (defined $q->param('B3'));
    $RC1 = $q->param('RC1') if (defined $q->param('RC1'));
    $RC2 = $q->param('RC2') if (defined $q->param('RC2'));
    $RC3 = $q->param('RC3') if (defined $q->param('RC3'));
    $BC1 = $q->param('BC1') if (defined $q->param('BC1'));
    $BC2 = $q->param('BC2') if (defined $q->param('BC2'));
    $BC3 = $q->param('BC3') if (defined $q->param('BC3'));
}

# process previous game results here
$stage += 1;

# determine prior ownership of switch and scale and score it
sub scoreOwnership() {

    if ($REDswitchL > $BLUEswitchL) {
	$REDscore += 5;
	$REDscore += 5 if ($stage == 2);
    }
    if ($REDscale > $BLUEscale) {
	$REDscore += 5;
	$REDscore += 5 if ($stage == 2);
    }
    if ($REDscale < $BLUEscale) {
	$BLUEscore += 5;
	$BLUEscore += 5 if ($stage == 2);
    }
    if ($REDswitchR < $BLUEswitchR) {
	$BLUEscore += 5;
	$BLUEscore += 5 if ($stage == 2);
    }
}

sub scoreRedRobot($) {
    my ($robot) = (@_);

    $REDswitchL++ if ($robot == 1);
    $REDscale++   if ($robot == 2);
    $REDswitchR++ if ($robot == 3);


    if ($robot == 4) {
	$REDforce++;
	$REDscore += 5;
    }
    if ($robot == 5) {
	$REDlevitate++;
	$REDscore += 5;
    }
    if ($robot == 6) {
	$REDboost++;
	$REDscore += 5;
    }
}

sub scoreBlueRobot($) {
    my ($robot) = (@_);

    $BLUEswitchR++ if ($robot == 1);
    $BLUEscale++   if ($robot == 2);
    $BLUEswitchL++ if ($robot == 3);


    if ($robot == 4) {
	$BLUEforce++;
	$BLUEscore += 5;
    }
    if ($robot == 5) {
	$BLUElevitate++;
	$BLUEscore += 5;
    }
    if ($robot == 6) {
	$BLUEboost++;
	$BLUEscore += 5;
    }
}

scoreOwnership();
scoreRedRobot($R1);
scoreRedRobot($R2);
scoreRedRobot($R3);
scoreBlueRobot($B1);
scoreBlueRobot($B2);
scoreBlueRobot($B3);
scoreOwnership();

# remove cubes from locations
sub removeCubes($$) {
    my ($robot, $color) = (@_);
    $pyramidL-- if ("$color" eq "red" && $robot == 1);
    $switchL-- if ("$color" eq "red" && $robot == 2);
    $pyramidR-- if ("$color" eq "blue" && $robot == 1);
    $switchR-- if ("$color" eq "blue" && $robot == 2);
    $REDportal-- if ("$color" eq "red" && $robot == 3 && $REDportal > 0);
    $BLUEportal-- if ("$color" eq "blue" && $robot == 3 && $BLUEportal > 0);
}

removeCubes($RC1, "red");
removeCubes($RC2, "red");
removeCubes($RC3, "red");
removeCubes($BC1, "blue");
removeCubes($BC2, "blue");
removeCubes($BC3, "blue");


# print the updated game and the form with the new form

print "<FORM METHOD=\"post\" ACTION=\"powerup.cgi\">\n";
print "<input type=\"hidden\" name=\"REDforce\" value=\"$REDforce\">\n";        # number of RED force cubes 0-3(4 = activated)
print "<input type=\"hidden\" name=\"REDlevitate\" value=\"$REDlevitate\">\n";  # number of RED levitate cubes 0-3(4 = activated)
print "<input type=\"hidden\" name=\"REDboost\" value=\"$REDboost\">\n";        # number of RED boost cubes 0-3(4 = activated)
print "<input type=\"hidden\" name=\"BLUEportal\" value=\"$BLUEportal\">\n";    # number of BLUE portal cubes 0-11
print "<input type=\"hidden\" name=\"REDrobot1\" value=\"$REDrobot1\">\n";      # RED robot 1 cube (1 to start)
print "<input type=\"hidden\" name=\"REDrobot2\" value=\"$REDrobot2\">\n";      # RED robot 2 cube (1 to start)
print "<input type=\"hidden\" name=\"REDrobot3\" value=\"$REDrobot3\">\n";      # RED robot 3 cube (1 to start)
print "<input type=\"hidden\" name=\"pyramidL\" value=\"$pyramidL\">\n";        # number of RED pyramid cubes (0-10)
print "<input type=\"hidden\" name=\"REDswitchL\" value=\"$REDswitchL\">\n";    # number of cubes on L switch RED plate
print "<input type=\"hidden\" name=\"BLUEswitchL\" value=\"$BLUEswitchL\">\n";  # number of cubes on L switch BLUE plate
print "<input type=\"hidden\" name=\"switchL\" value=\"$switchL\">\n";          # number of cubes at L switch (0-6)
print "<input type=\"hidden\" name=\"REDscale\" value=\"$REDscale\">\n";        # number of cubes on RED scale plate
print "<input type=\"hidden\" name=\"BLUEscale\" value=\"$BLUEscale\">\n";      # number of cubes on BLUE scale plate
print "<input type=\"hidden\" name=\"switchR\" value=\"$switchR\">\n";          # number of cubes at R switch (0-6)
print "<input type=\"hidden\" name=\"REDswitchR\" value=\"$REDswitchR\">\n";    # number of cubes on R switch RED plate
print "<input type=\"hidden\" name=\"BLUEswitchR\" value=\"$BLUEswitchR\">\n";  # number of cubes on R switch BLUE plate
print "<input type=\"hidden\" name=\"pyramidR\" value=\"$pyramidR\">\n";        # number of BLUE pyramid cubes (0-10)    
print "<input type=\"hidden\" name=\"BLUErobot1\" value=\"$BLUErobot1\">\n";    # BLUE robot 1 cube (1 to start)                                                                             
print "<input type=\"hidden\" name=\"BLUErobot2\" value=\"$BLUErobot2\">\n";    # BLUE robot 2 cube (1 to start)                                                                             
print "<input type=\"hidden\" name=\"BLUErobot3\" value=\"$BLUErobot3\">\n";    # BLUE robot 3 cube (1 to start)                                                                             
print "<input type=\"hidden\" name=\"REDportal\" value=\"$REDportal\">\n";      # number of RED portal cubes 0-11                                                                            
print "<input type=\"hidden\" name=\"BLUEforce\" value=\"$BLUEforce\">\n";      # number of BLUE force cubes 0-3(4 = activated)                                                              
print "<input type=\"hidden\" name=\"BLUElevitate\" value=\"$BLUElevitate\">\n";# number of BLUE levitate cubes 0-3(4 = levitate)                                                            
print "<input type=\"hidden\" name=\"BLUEboost\" value=\"$BLUEboost\">\n";      # number of BLUE boost cubes 0-3(4 = levitate)                                                               
print "<input type=\"hidden\" name=\"stage\" value=\"$stage\">\n";              # timed stage number                                                                                         
print "<input type=\"hidden\" name=\"REDscore\" value=\"$REDscore\">\n";        # RED score    
print "<input type=\"hidden\" name=\"BLUEscore\" value=\"$BLUEscore\">\n";      # BLUE score   

print "<table cellspacing=0 cellpadding=0 border=0><tr><td colspan=2>\n";
print "<div style=\"position:relative; background:url(field.png); no-repeat left top; width: 917px; height:477px;\">\n";

#switch/scale scoring                                                                          
print "<div style=\"position:absolute; top:132px; left:290px; color:yellow;\"><B>$REDswitchL</B></div>\n";
print "<div style=\"position:absolute; top:242px; left:290px; color:yellow;\"><B>$BLUEswitchL</B></div>\n";
print "<div style=\"position:absolute; top:115px; left:445px; color:yellow;\"><B>$BLUEscale</B></div>\n";
print "<div style=\"position:absolute; top:260px; left:445px; color:yellow;\"><B>$REDscale</B></div>\n";
print "<div style=\"position:absolute; top:132px; right:310px; color:yellow;\"><B>$REDswitchR</B></div>\n";
print "<div style=\"position:absolute; top:242px; right:310px; color:yellow;\"><B>$BLUEswitchR</B></div>\n";

# RED vault
print "<div style=\"position:absolute; top:135px; left:15px;\"><IMG SRC=cube.png></div>\n" if ($REDforce == 3);
print "<div style=\"position:absolute; top:165px; left:15px;\"><IMG SRC=cube.png></div>\n" if ($REDforce > 1 && $REDforce < 4);
print "<div style=\"position:absolute; top:195px; left:15px;\"><IMG SRC=cube.png></div>\n" if ($REDforce > 0 && REDforce < 4);

print "<div style=\"position:absolute; top:135px; left:45px;\"><IMG SRC=cube.png></div>\n" if ($REDlevitate == 3);
print "<div style=\"position:absolute; top:165px; left:45px;\"><IMG SRC=cube.png></div>\n" if ($REDlevitate > 1 && $REDlevitate < 4);
print "<div style=\"position:absolute; top:195px; left:45px;\"><IMG SRC=cube.png></div>\n" if ($REDlevitate > 0 && $REDlevitate < 4);

print "<div style=\"position:absolute; top:135px; left:75px;\"><IMG SRC=cube.png></div>\n" if ($REDboost == 3);
print "<div style=\"position:absolute; top:165px; left:75px;\"><IMG SRC=cube.png></div>\n" if ($REDboost > 1 && $REDboost < 4);
print "<div style=\"position:absolute; top:195px; left:75px;\"><IMG SRC=cube.png></div>\n" if ($REDboost > 0 && $REDboost < 4);

# BLUE portal
print "<div style=\"position:absolute; top:20px; left:105px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 10);
print "<div style=\"position:absolute; top:20px; left:120px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 9);
print "<div style=\"position:absolute; top:20px; left:135px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 8);
print "<div style=\"position:absolute; top:20px; left:150px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 7);
print "<div style=\"position:absolute; top:35px; left:105px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 6);
print "<div style=\"position:absolute; top:360px; left:105px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 5);
print "<div style=\"position:absolute; top:360px; left:120px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 4);
print "<div style=\"position:absolute; top:360px; left:135px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 3);
print "<div style=\"position:absolute; top:360px; left:150px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 2);
print "<div style=\"position:absolute; top:345px; left:105px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 1);
print "<div style=\"position:absolute; top:345px; left:120px;\"><IMG SRC=cube.png></div>\n" if ($BLUEportal > 0);

# RED robots
print "<div style=\"position:absolute; top:95px; left:140px;\"><IMG SRC=cube.png></div>\n" if ($stage == 1);
print "<div style=\"position:absolute; top:215px; left:140px;\"><IMG SRC=cube.png></div>\n" if ($stage == 1);
print "<div style=\"position:absolute; top:285px; left:140px;\"><IMG SRC=cube.png></div>\n" if ($stage == 1);

# RED pyramid
print "<div style=\"position:absolute; top:205px; left:260px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 0);
print "<div style=\"position:absolute; top:190px; left:260px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 1);
print "<div style=\"position:absolute; top:175px; left:260px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 2);
print "<div style=\"position:absolute; top:198px; left:245px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 3);
print "<div style=\"position:absolute; top:182px; left:245px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 4);
print "<div style=\"position:absolute; top:190px; left:230px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 5);
print "<div style=\"position:absolute; top:198px; left:255px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 6);
print "<div style=\"position:absolute; top:182px; left:255px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 7);
print "<div style=\"position:absolute; top:190px; left:240px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 8);
print "<div style=\"position:absolute; top:190px; left:250px;\"><IMG SRC=cube.png></div>\n" if ($pyramidL > 9);



# RED switch cubes
print "<div style=\"position:absolute; top:120px; left:330px;\"><IMG SRC=cube.png></div>\n" if ($switchL > 5);
print "<div style=\"position:absolute; top:148px; left:330px;\"><IMG SRC=cube.png></div>\n" if ($switchL > 4);
print "<div style=\"position:absolute; top:175px; left:330px;\"><IMG SRC=cube.png></div>\n" if ($switchL > 3);
print "<div style=\"position:absolute; top:205px; left:330px;\"><IMG SRC=cube.png></div>\n" if ($switchL > 2);
print "<div style=\"position:absolute; top:232px; left:330px;\"><IMG SRC=cube.png></div>\n" if ($switchL > 1);
print "<div style=\"position:absolute; top:260px; left:330px;\"><IMG SRC=cube.png></div>\n" if ($switchL > 0);


# BLUE switch cubes
print "<div style=\"position:absolute; top:120px; right:340px;\"><IMG SRC=cube.png></div>\n" if ($switchR > 5);
print "<div style=\"position:absolute; top:148px; right:340px;\"><IMG SRC=cube.png></div>\n" if ($switchR > 4);
print "<div style=\"position:absolute; top:175px; right:340px;\"><IMG SRC=cube.png></div>\n" if ($switchR > 3);
print "<div style=\"position:absolute; top:205px; right:340px;\"><IMG SRC=cube.png></div>\n" if ($switchR > 2);
print "<div style=\"position:absolute; top:232px; right:340px;\"><IMG SRC=cube.png></div>\n" if ($switchR > 1);
print "<div style=\"position:absolute; top:260px; right:340px;\"><IMG SRC=cube.png></div>\n" if ($switchR > 0);


# BLUE pyramid
print "<div style=\"position:absolute; top:175px; right:270px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 0);
print "<div style=\"position:absolute; top:190px; right:270px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 1);
print "<div style=\"position:absolute; top:205px; right:270px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 2);
print "<div style=\"position:absolute; top:182px; right:255px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 3);
print "<div style=\"position:absolute; top:198px; right:255px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 4);
print "<div style=\"position:absolute; top:190px; right:240px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 5);
print "<div style=\"position:absolute; top:182px; right:265px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 6);
print "<div style=\"position:absolute; top:198px; right:265px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 7);
print "<div style=\"position:absolute; top:190px; right:250px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 8);
print "<div style=\"position:absolute; top:190px; right:260px;\"><IMG SRC=cube.png></div>\n" if ($pyramidR > 9);


# BLUE robots
print "<div style=\"position:absolute; top:95px; right:150px;\"><IMG SRC=cube.png></div>\n" if ($stage == 1);
print "<div style=\"position:absolute; top:165px; right:150px;\"><IMG SRC=cube.png></div>\n" if ($stage == 1);
print "<div style=\"position:absolute; top:285px; right:150px;\"><IMG SRC=cube.png></div>\n" if ($stage == 1);


# RED portal
print "<div style=\"position:absolute; top:20px; right:115px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 10);
print "<div style=\"position:absolute; top:20px; right:130px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 9);
print "<div style=\"position:absolute; top:20px; right:145px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 8);
print "<div style=\"position:absolute; top:20px; right:160px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 7);
print "<div style=\"position:absolute; top:35px; right:115px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 6);
print "<div style=\"position:absolute; top:360px; right:115px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 5);
print "<div style=\"position:absolute; top:360px; right:130px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 4);
print "<div style=\"position:absolute; top:360px; right:145px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 3);
print "<div style=\"position:absolute; top:360px; right:160px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 2);
print "<div style=\"position:absolute; top:345px; right:115px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 1);
print "<div style=\"position:absolute; top:345px; right:130px;\"><IMG SRC=cube.png></div>\n" if ($REDportal > 0);


# BLUE force
print "<div style=\"position:absolute; top:135px; right:80px;\"><IMG SRC=cube.png></div>\n" if ($BLUEforce == 3);
print "<div style=\"position:absolute; top:165px; right:80px;\"><IMG SRC=cube.png></div>\n" if ($BLUEforce > 1);
print "<div style=\"position:absolute; top:195px; right:80px;\"><IMG SRC=cube.png></div>\n" if ($BLUEforce > 0);

# BLUE levitate
print "<div style=\"position:absolute; top:135px; right:50px;\"><IMG SRC=cube.png></div>\n" if ($BLUElevitate == 3);
print "<div style=\"position:absolute; top:165px; right:50px;\"><IMG SRC=cube.png></div>\n" if ($BLUElevitate > 1);
print "<div style=\"position:absolute; top:195px; right:50px;\"><IMG SRC=cube.png></div>\n" if ($BLUElevitate > 0);

# BLUE boost
print "<div style=\"position:absolute; top:135px; right:20px;\"><IMG SRC=cube.png></div>\n" if ($BLUEboost == 3);
print "<div style=\"position:absolute; top:165px; right:20px;\"><IMG SRC=cube.png></div>\n" if ($BLUEboost > 1);
print "<div style=\"position:absolute; top:195px; right:20px;\"><IMG SRC=cube.png></div>\n" if ($BLUEboost > 0);

print "</div></td></tr><tr>\n";
#print "<th><H3><div style=\"color:red\">Red Alliance: $REDscore</div></H3>\n";
#print "</th><th>\n";
#print "<H3><div style=\"color:blue\">Blue Alliance: $BLUEscore</div></H3>\n";
#print "</th></tr>\n";
print "<td colspan=2>";
print "<table width=\"100%\" border=0><tr>";
print "<th><H3><div style=\"color:red\">Red Alliance: $REDscore</div></H3>\n";
my $time = "2:30";
$time = "2:15" if ($stage == 2);
$time = "2:05" if ($stage == 3);
$time = "1:55" if ($stage == 4);
$time = "1:45" if ($stage == 5);
$time = "1:35" if ($stage == 6);
$time = "1:25" if ($stage == 7);
$time = "1:15" if ($stage == 8);
$time = "1:05" if ($stage == 9);
$time = ":55" if ($stage == 10);
$time = ":45" if ($stage == 11);
$time = ":35" if ($stage == 12);
$time = ":25" if ($stage == 13);
$time = ":15" if ($stage == 14);
$time = ":00" if ($stage > 14);
print "</th><th>Time: $time</th><th>\n";
print "<H3><div style=\"color:blue\">Blue Alliance: $BLUEscore</div></H3>\n";
print "</tr></table></td></tr>\n";

sub printPickup($$$) {
    my ($pyramid, $switch, $portal) = (@_);
    print "<option value=\"0\">nowhere</option>\n";
    print "<option value=\"1\">pyramid</option>\n" if ($pyramid > 0);
    print "<option value=\"2\">switch edge</option>\n" if ($switch > 0);
    print "<option value=\"3\">portal</option>\n" if ($portal > 0);
}

sub printOptions($$$$) {
    my ($color, $force, $levitate, $boost) = (@_);

    print "<option value=\"0\">nowhere</option>\n";
    print "<option value=\"1\">own switch $color plate</option>\n";
    print "<option value=\"2\">scale $color plate</option>\n";
    print "<option value=\"3\">opposing switch $color plate</option>\n";
    print "<option value=\"4\">exchange/vault for Force</option>\n" if ($force < 4);
    print "<option value=\"5\">exchange/vault for Levitate</option>\n" if ($levitate < 4);
    print "<option value=\"6\">exchange/vault for Boost</option>\n" if ($boost < 4);
}

print "<tr><td>\n";
if ($stage == 1) {
    print "<p>Red Robot #1 places its cube\n";
} else {
    print "<p>Red #1 from";
    print "<select name=\"RC1\">\n";
    printPickup($pyramidL, $switchL, $REDportal);
    print "</select>to";
}
print "<select name=\"R1\">\n";
printOptions("red", $REDforce, $REDlevitate, $REDboost);
print "</select></p></td><td>\n";

if ($stage == 1) {
    print "<p>Blue Robot #1 places its cube\n";
} else {
    print "<p>Blue #1 from";
    print "<select name=\"BC1\">\n";
    printPickup($pyramidR, $switchR, $BLUEportal);
    print "</select>to";
}
print "<select name=\"B1\">\n";
printOptions("blue", $BLUEforce, $BLUElevitate, $BLUEboost);
print "</select></p></td><td></tr><tr><td>\n";

if ($stage == 1) {
    print "<p>Red Robot #2 places its cube\n";
} else {
    print "<p>Red #2 from";
    print "<select name=\"RC2\">\n";
    printPickup($pyramidL, $switchL, $REDportal);
    print "</select>to";
}
print "<select name=\"R2\">\n";
printOptions("red", $REDforce, $REDlevitate, $REDboost);
print "</select></p></td><td>\n";

if ($stage == 1) {
    print "<p>Blue Robot #2 places its cube\n";
} else {
    print "<p>Blue #2 from";
    print "<select name=\"BC2\">\n";
    printPickup($pyramidR, $switchR, $BLUEportal);
    print "</select>to";
}
print "<select name=\"B2\">\n";
printOptions("blue", $BLUEforce, $BLUElevitate, $BLUEboost);
print "</select></p></td><td></tr><tr><td>\n";

if ($stage == 1) {
    print "<p>Red Robot #3 places its cube\n";
} else {
    print "<p>Red #3 from";
    print "<select name=\"RC3\">\n";
    printPickup($pyramidL, $switchL, $REDportal);
    print "</select>to";
}
print "<select name=\"R3\">\n";
printOptions("red", $REDforce, $REDlevitate, $REDboost);
print "</select></p></td><td>\n";

if ($stage == 1) {
    print "<p>Blue Robot #3 places its cube\n";
} else {
    print "<p>Blue #3 from";
    print "<select name=\"BC3\">\n";
    printPickup($pyramidR, $switchR, $BLUEportal);
    print "</select>to";
}
print "<select name=\"B3\">\n";
printOptions("blue", $BLUEforce, $BLUElevitate, $BLUEboost);
print "</select></p></td></tr><tr>\n";

print "<td colspan=2 align=center><p>\n";
print "<input type=\"submit\" value=\"Submit Selections\">\n";
print "</p></tr></table>\n";
print "<p>&nbsp;</p>\n";
print "</BODY></HTML>\n";


