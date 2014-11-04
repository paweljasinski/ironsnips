using System;

namespace dotnetenums {
    public class DotNetEnums {
        public enum Days {Sat, Sun, Mon, Tue, Wed, Thu, Fri};
        public static Days day = Days.Sat;

        public Days instanceDay;

        public DotNetEnums() {
            instanceDay = Days.Wed;
        }
    }

}
