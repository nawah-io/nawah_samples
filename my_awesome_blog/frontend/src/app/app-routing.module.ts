import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminBlogEditComponent } from './admin-blog-edit/admin-blog-edit.component';
import { AdminBlogListComponent } from './admin-blog-list/admin-blog-list.component';
import { AdminBlogNewComponent } from './admin-blog-new/admin-blog-new.component';
import { AdminCommentPendingListComponent } from './admin-comment-pending-list/admin-comment-pending-list.component';
import { AdminContainerComponent } from './admin-container/admin-container.component';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { HomeComponent } from './home/home.component';


const routes: Routes = [
	{ path: '', redirectTo: '/home', pathMatch: 'full' },
	{ path: 'home', component: HomeComponent },
	{
		path: 'admin', component: AdminContainerComponent, children: [
			{ path: '', redirectTo: '/admin/login', pathMatch: 'full' },
			{ path: 'login', component: AdminLoginComponent },
			{ path: 'dashboard', component: AdminDashboardComponent },
			{ path: 'blog-new', component: AdminBlogNewComponent },
			{ path: 'blog-list', component: AdminBlogListComponent },
			{ path: 'blog-edit/:_id', component: AdminBlogEditComponent },
			{ path: 'comment-list', component: AdminCommentPendingListComponent },
		]
	},
];

@NgModule({
	imports: [RouterModule.forRoot(routes)],
	exports: [RouterModule]
})
export class AppRoutingModule { }
