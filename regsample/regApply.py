from regsample.regpractice import RegPractice

newword = RegPractice().dividedBy3();

wordneedreplaceword = "admin inst"
newword = RegPractice().replace_special_word(wordneedreplaceword)

wordneedremove = "This is shares, please try"
newword = RegPractice().remove_special_word(wordneedremove)

charneedremove = "This,is,@;for & test."
newword = RegPractice().remove_special_char(charneedremove)

wordneedclearbracket = "Test (word) to (remove bracket), just try"
newword = RegPractice().clear_brackets(wordneedclearbracket)

wordneedreplacechar = "This is-the/word : let's have a look - "
newword = RegPractice().replace_special_char(wordneedreplacechar)


