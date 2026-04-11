Modern Date and Time
====================

Older Java code often uses ``Date`` and ``Calendar``. Newer code should prefer
the ``java.time`` package because it separates dates, times, time zones, and
durations into clearer types.

Dates and times
---------------

Use ``LocalDate`` when you need only a calendar date. Use ``LocalTime`` when
you need only a clock time. Use ``LocalDateTime`` when you need both, but no
time zone.

.. code-block:: java

   import java.time.LocalDate;
   import java.time.LocalDateTime;
   import java.time.LocalTime;

   LocalDate date = LocalDate.of(2026, 4, 10);
   LocalTime time = LocalTime.of(14, 30);
   LocalDateTime timestamp = LocalDateTime.of(date, time);

   System.out.println(date);
   System.out.println(time);
   System.out.println(timestamp);

Instants and time zones
-----------------------

Use ``Instant`` for a point on the global timeline. Use ``ZonedDateTime`` when
the time zone matters to humans.

.. code-block:: java

   import java.time.Instant;
   import java.time.ZoneId;
   import java.time.ZonedDateTime;

   Instant now = Instant.now();
   ZonedDateTime local = now.atZone(ZoneId.of("America/New_York"));

   System.out.println(now);
   System.out.println(local);

Durations and periods
---------------------

Use ``Duration`` for clock-based amounts of time. Use ``Period`` for
calendar-based amounts of time.

.. code-block:: java

   import java.time.Duration;
   import java.time.LocalDate;
   import java.time.LocalDateTime;
   import java.time.Period;

   Duration ninetyMinutes = Duration.ofMinutes(90);
   LocalDateTime end = LocalDateTime.now().plus(ninetyMinutes);

   Period oneMonth = Period.ofMonths(1);
   LocalDate nextMonth = LocalDate.now().plus(oneMonth);

   System.out.println(end);
   System.out.println(nextMonth);

Formatting and parsing
----------------------

``DateTimeFormatter`` converts date/time objects to strings and parses strings
back into date/time objects.

.. code-block:: java

   import java.time.LocalDate;
   import java.time.format.DateTimeFormatter;

   DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");

   LocalDate date = LocalDate.parse("04/10/2026", formatter);
   String text = date.format(formatter);

   System.out.println(date);
   System.out.println(text);

Use ISO-8601 strings such as ``2026-04-10`` when possible. They sort naturally
and are usually easier for programs to exchange.
