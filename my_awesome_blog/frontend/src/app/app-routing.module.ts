import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomePage } from './pages/home/home.page';

import { AdminContainerComponent } from './shared/admin-container/admin-container.component';
import { AdminLoginPage } from './pages/admin-login/admin-login.page';
import { AdminDashboardPage } from './pages/admin-dashboard/admin-dashboard.page';
import { AdminBlogNewPage } from './pages/admin-blog-new/admin-blog-new.page';
import { AdminBlogListPage } from './pages/admin-blog-list/admin-blog-list.page';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomePage },

  {
    path: 'admin', component: AdminContainerComponent, children: [
      { path: '', redirectTo: '/admin/login', pathMatch: 'full' },
      { path: 'login', component: AdminLoginPage },
      { path: 'dashboard', component: AdminDashboardPage },
      { path: 'blog-new', component: AdminBlogNewPage },
      { path: 'blog-list', component: AdminBlogListPage },
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
