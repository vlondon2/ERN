import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "pages/Home";
import NotFound from "pages/NotFound";
const CONFIRMATION = React.lazy(() => import("pages/CONFIRMATION"));
const REPORT = React.lazy(() => import("pages/REPORT"));
const REPORTpopup = React.lazy(() => import("pages/REPORTpopup"));
const HOME1 = React.lazy(() => import("pages/HOME1"));
const ProjectRoutes = () => {
  return (
    <React.Suspense fallback={<>Loading...</>}>
      <Router>
        <Routes>
          <Route path="/" element={<HOME1 />} />
          <Route path="*" element={<NotFound />} />
          <Route path="/reportpopup" element={<REPORTpopup />} />
          <Route path="/report" element={<REPORT />} />
          <Route path="/confirmation" element={<CONFIRMATION />} />
          <Route path="/dhiwise-dashboard" element={<Home />} />
        </Routes>
      </Router>
    </React.Suspense>
  );
};
export default ProjectRoutes;
