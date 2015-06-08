                   / WODDER /

                 a prototype application 


    ~ What is Wodder?

      A sqlite powered WOD (Work Out of the Day) generator application

    ~ How do I use it?

      1. edit the configuration in the wodder.py file or
         export an FLASKR_SETTINGS environment variable
         pointing to a configuration file.

      2. initialize the database with this command:

         wodder --app=wodder initdb

      3. now you can run wodder:

         wodder --app=wodder run

         the application will greet you on
         http://localhost:5000/

    ~ Is it tested?

      You betcha.  Run the `wodder_test.py` file to see
      the tests pass.