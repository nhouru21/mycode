#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

   def main():
       marvelchars= {
               "Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


       cn = input("what name?")
       cs = input("what stat?")

       print(marvelchars.get(cn).get(cs))
       
 main()
